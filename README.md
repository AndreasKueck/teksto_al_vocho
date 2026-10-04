# Per MacroDroid krei sondosieron el teksto

Tiu chi GitHub-deponejo entenas [MacroDroid](https://www-macrodroid-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=eo&_x_tr_hl=de&_x_tr_pto=wapp)-makroon, kiu

1. atendas enigon de skriba teksto kaj
2. el ghi kreas sondosieron `vocho.mp3`, nome per la OpenAI-modelo `gpt-4o-mini-tts`.

---

## Antaukondichoj

Antau ol uzi la makroon, certigu, ke MacroDroid estas instalitaj kaj ghuste agordita.

Krome la uzanto bezonas validan OpenAI-API-shlosilon por la parolsintezo. Ghi funkcias per modelo `gpt-4o-mini-tts`.

## Importi la makroon

1. Elshutu makroon [teksto_al_vocho](https://www.dropbox.com/scl/fi/jhedhg0n4tqswq4lsfmzy/teksto_al_vocho.macro?rlkey=l4q9fg61b0nw0yv1ydvoq43qr&st=4fa9a9vd&dl=0) en vian smartfonon.
2. Malfermu apon MacroDroid.
3. En ghin importu la elshutitan makroo-dosieron `teksto_al_vocho.macro` trovighantan en via smartfono.
4. En ago `Shell Script` anstatauigu la shablonan OpenAI-API-shlosilon per valida OpenAI-API-shlosilo kaj konservu chion.
5. Donu chiujn necesajn permesojn al MacroDroid.

## Dosierujo por la sondosieroj

Por la sondosieroj `vocho.mp3` la makroo uzas dosierujon `/storage/emulated/0/dosierujo/` en la interna memoro de Android.

Certigu, ke tiu dosierujo ekzistas kaj tiucele estas uzebla.

## Alternativo per realtempa API de OpenAI

Konsidere la anoncitan [evitindigon](https://developers.openai.com/api/docs/deprecations) de interalie `gpt-4o-mini-tts` jen alternativa parolsintezo per modelo `gpt-realtime-2.1-tts`:
Temas pri makroo [teksto_al_vocho_per_realtempa_api_2.macro](https://www.dropbox.com/scl/fi/yiedyn1kbkweane6l3rwx/teksto_al_vocho_per_realtempa_api_2.macro?rlkey=9pa349lqxwyo4klvysjfrz541&st=9y5thi8e&dl=0) kombine kun la Pitona programo `realtime_tts.py`; la fontokodoj estas troveblaj [tie](https://github.com/AndreasKueck/teksto_al_vocho/tree/main/alternativo_per_realtempa_api). La Pitona programo estu efektivigita kadre de Android-apo Termux. Pri ghi jen [pli](https://github.com/AndreasKueck/transskribi_amr#).

## Vochlegigi tekston kunhavigitan al MacroDroid el alia apo

Tion oni povas fari per la makroo `vochlegigi.macro` ([elshuti](https://www.dropbox.com/scl/fi/7xdc5stdz6six1cgj0s0a/vochlegigi.macro?rlkey=e9lohnjbcknqkoe4a3qdof100&st=doz9b6xo&dl=0)).

## Permesilo ("License")

Chi tiu projekto estas publikigita sub la [MIT-permesilo](./LICENSE).

Vi estas libera uzi, modifi kaj distribui chi tiun projekton, se vi konservas la kopirajtan avizon.
