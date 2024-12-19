#A high contrast theme for python code in ReadTheDocs
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic

class HighContrastTheme(Style):
    """A custom Pygments style inspired by VS Code High Contrast."""
    background_color = "#f98f87"
    default_style = ""

    styles = {
        Comment:            'italic #6A9955',
        Keyword:            'bold #569CD6',
        Name.Function:      '#4EC9B0',
        Name.Variable:      '#9CDCFE',
        String:             '#D69D85',
        Number:             '#B5CEA8',
        Operator:           '#D4D4D4',
        Generic.Heading:    'bold #FFFFFF',
        Generic.Subheading: 'bold #FFFFFF',
        Error:              'bg:#FF0000 #FFFFFF',
    }
