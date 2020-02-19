$(document).ready(function() {
  $('#box11').val($.cookie('box11'));
  $('#box12').val($.cookie('box12'));
  $('#box13').val($.cookie('box13'));
  $('#box14').val($.cookie('box14'));
  $('#box15').val($.cookie('box15'));
  $("#submit").click(function() {
    $.cookie('box11', $('#box11')[0].value);
    $.cookie('box12', $('#box12')[0].value);
    $.cookie('box13', $('#box13')[0].value);
    $.cookie('box14', $('#box14')[0].value);
    $.cookie('box15', $('#box15')[0].value);
  })
  setSize();
})
$(window).resize(setSize)

function setSize() {
  // 基本となるサイズの取得
  const size = $('body').outerWidth() * 0.6;

  //右上の矢印
  $('#loginguide-img').width(size * 0.14)
  $('#loginguide-img').offset({
    top: $('#header').outerHeight() + $('#header-name').outerHeight(),
    left: $('body').outerWidth() - $('#header-login').outerWidth() / 2 - $('#loginguide-img').outerWidth() / 2
  });

  // 天使のサイズ
  $('#engelimg').height($('#engelballoon').height() * 0.8)

  // 問題3の文字サイズ

  $('.q3table').css({ 'font-size': $('.q3table').width() * 0.8 });
}