from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./src/templates")
templates.env.block_start_string += ' '
templates.env.variable_start_string += ' '
templates.env.comment_start_string += ' '

templates.env.block_end_string = ' ' + templates.env.block_end_string
templates.env.variable_end_string = ' ' + templates.env.variable_end_string
templates.env.comment_end_string = ' ' + templates.env.comment_end_string

# 避免与 Vue 冲突
