from pathlib import Path
from html.parser import HTMLParser
from datetime import date, timedelta
import json
root=Path(__file__).resolve().parent.parent
class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.local=[]; self.anchors=[]; self.days=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='details' and a.get('class')=='day': self.days.append(a['id'])
        if tag=='img':
            assert a.get('alt'), 'Image missing description'
            assert a.get('width') and a.get('height'), 'Image missing reserved dimensions'
        if a.get('target')=='_blank': assert 'noopener' in a.get('rel','')
        for key in ('src','href'):
            value=a.get(key,'')
            if value.startswith('#'): self.anchors.append(value[1:])
            elif value and not value.startswith(('http:','https:','data:')): self.local.append(value)
html=(root/'index.html').read_text(); audit=Audit(); audit.feed(html)
assert len(audit.ids)==len(set(audit.ids)), 'Duplicate IDs'
assert len(audit.days)==16
assert set(audit.anchors).issubset(audit.ids), 'Broken section link'
for f in audit.local: assert (root/f).is_file(),f'Missing asset: {f}'
for bad in ['Grand Canyon','Lite Flight','LA helicopter','two helicopter','PHOTO_CREDITS','being prepared']:
    assert bad.lower() not in html.lower(),f'Stale content: {bad}'
data=json.loads((root/'scripts/itinerary.json').read_text())
assert [d['date'] for d in data]==[(date(2026,9,9)+timedelta(days=i)).isoformat() for i in range(16)]
assert [d['city'] for d in data]==['sf']*4+['la']*2+['vegas']+['nyc']*9
print('Verified: 16 consecutive calendar dates, requested destinations, corrected exclusions, section links, image metadata and local assets.')
