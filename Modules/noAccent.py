from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def noAccent(txt: str, feature, parent):
    """
    Remove spanish accents:
    <h2>Example usage:</h2>
    <ul>
      <li>noAccent("corazon") -> "CORAZON"</li>
      <li>noAccent("educacion") -> "EDUCACION"</li>
    </ul>
    """
    accent = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u'
    }
    ans = txt.lower()
    for k,v in accent.items():
        ans = ans.replace(k, v)
    return ans.upper()