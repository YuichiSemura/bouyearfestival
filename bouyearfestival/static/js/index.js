$(document).ready(setSize)
$(window).resize(setSize)
$(window).on('touchmove.noScroll', function(e) {
  e.preventDefault();
});

function setSize() {
  // 基本となる手紙のサイズの取得
  const height = $('body').outerHeight() - $('#header').outerHeight() - $('#footer').outerHeight();
  const width = $('body').outerWidth();
  const size = (height < width ? height : width) * 0.6;

  // 手紙
  $('#letterpack').offset({
    top: $('body').outerHeight() / 2 - $('#letterpack').outerHeight() / 2,
    left: $('body').outerWidth() / 2 - $('#letterpack').outerWidth() / 2
  });
  $('#letterimg').width(size)
  $('#letterimg').height(size)
  $('#tap').width(size)
  $('#tap').height(size)
  $('#tap').css("fontSize", String(size * 0.16) + "px");

  //message
  standardSize = $('body').outerWidth() * 0.7;
  minSize = size * 1.17;
  $('#message').width(standardSize > minSize ? minSize : standardSize);
  $('#message p').css("fontSize", String(size * 0.06) + "px");

  //右上の矢印
  $('#loginguide-img').width(size * 0.2)
  $('#loginguide').offset({
    top: $('#header').outerHeight(),
    left: $('body').outerWidth() - $('#header-login').outerWidth() / 2 - $('#loginguide-img').outerWidth() / 2
  });

  // フッターの場所
  $('#footer').offset({
    top: $('body').outerHeight() - $('#footer').outerHeight()
  });
}