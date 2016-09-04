# salt_parser
`
sudo salt "*" state.single pkg.installed name=bash  --out json | python parsjsnon.py 
Minion: fedora-thinkpad rpm: bash result: True

`
