from IPython.display import display, HTML
import pandas as pd
from jupyterquiz import display_quiz

class Worksheet:
    def __init__(self,worksheet_num:str):
        hints = pd.read_excel(f'worksheet_{worksheet_num}.xlsx')
        self.path_to_quiz_prefix = f'worksheet_{worksheet_num}'
        self.hint = self.Hint(hints, worksheet_num)
    def quiz(self, ref_id:str):
        #question_dict or 'https://path.to/file.json'
        try:
            display_quiz(f'{self.path_to_quiz_prefix}_{ref_id}.json')
        except:
            pass
    class Hint:
        def __init__(self, hints, worksheet_num):
            self.hints_df = hints
            self.worksheet_num = worksheet_num
        def __get(self, ref_id:str, default=None)->str:
            df = self.hints_df
            r = default
            if len(df[df['Ref']==ref_id])>0:
                r = self.hints_df.set_index('Ref').loc[ref_id,'Hint']
            return r if r else default
        def __display_hint_cell_text( self, hint_text, ref_id ):
            if hint_text:
                js_code = """
                <script>
                function toggleCell(w_id,ref_id) {
                    var cell = document.getElementById('cell_to_toggle_'+w_id+':'+ref_id);
                    var button = document.getElementById('toggle_button_'+w_id+':'+ref_id);
                    if (cell.style.display === 'none') {
                        cell.style.display = 'block';
                        button.innerHTML = 'Hide Hint';
                    } else {
                        cell.style.display = 'none';
                        button.innerHTML = 'Show Hint';
                    }
                }
                </script>
                """ 
                html_code = f"""
                <button id="toggle_button_{self.worksheet_num}:{ref_id}" onclick="toggleCell('{self.worksheet_num}','{ref_id}')">Show Hint</button>
                <div id="cell_to_toggle_{self.worksheet_num}:{ref_id}" style="display: none;">
                    {hint_text}
                </div>
                """
                display(HTML(js_code + html_code))
        def offer( self, question_ref ):
            return self.__display_hint_cell_text( self.__get(question_ref), question_ref )
