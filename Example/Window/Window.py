import PySimpleGUI as psgui

# ウィンドウに載せるレイアウトを構築
layout = [
  [psgui.Text('Free Text.', text_color='#00F000')],
  [psgui.InputText(key='ipt-key')],
  [psgui.Button('Button', key='btn-key')],
]

# ウィンドウ生成
window = psgui.Window(
  'Window title.',
  layout,
  size=(300, 200),
  finalize=True
)

# 無限ループ
while True:
  # イベントの入力待ち
  event, values = window.read()

  # ボタンを押された時のイベント
  if event == 'btn-key':
    msg = values['ipt-key']
    psgui.popup(msg)

  # ウィンドウのクローズ処理
  if event == psgui.WIN_CLOSED or event == 'Exit':
    break

# ウィンドウのクローズ処理
window.close()