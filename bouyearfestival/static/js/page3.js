$(document).ready(setSize)
$(window).resize(setSize)

function setSize() {
  // 基本となるサイズの取得
  const size = $('body').outerWidth() * 0.6;

  // 天使のサイズ
  $('#engelimg').height($('#engelballoon').height())
}