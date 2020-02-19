function color_inversion(id) {
  if (document.getElementById(id).value == "blue") {
    document.getElementById(id).style.background = "#FFF262";
    document.getElementById(id).style.border = "solid #eccf29";
    document.getElementById(id).value = "yellow";
  } else {
    document.getElementById(id).style.background = "#add7f3";
    document.getElementById(id).style.border = "solid #4ec6db";
    document.getElementById(id).value = "blue";
  }
}

function color_reset() {
  var btns = document.getElementsByClassName('q1_btn');
  var btns_num = btns.length;
  for (j = 0; j < btns_num; j++) {
    btns.item(j).style.background = "#add7f3";
    btns.item(j).style.border = "solid #4ec6db";
    btns.item(j).value = "blue";
  }
  this.color_inversion("q1_60");
}

// 表の動的作成
function makeTable(data, tableId) {
  // 表の作成開始
  var rows = [];
  var table = document.createElement("table");

  // 表に2次元配列の要素を格納
  for (i = 0; i < data.length; i++) {
    rows.push(table.insertRow(-1)); // 行の追加
    for (j = 0; j < data[0].length; j++) {
      cell = rows[i].insertCell(-1);
      var button = document.createElement("button");
      button.id = 'q1_' + i + j;
      button.classList.add("q1_btn");
      button.onclick = function() { color_inversion(this.id) };
      button.innerText = data[i][j];
      cell.appendChild(button);
    }
  }
  // 指定したdiv要素に表を加える
  document.getElementById(tableId).appendChild(table);
}

$(document).ready(function() {
  // 表のデータ
  var sideLength = 7;
  var sentence = '読んでさらつ。、ない上かなけはい四をむぐだえ答文字に中のら。たし隠おり人のしまいしの犯氏名は忘年会';
  var data = [];
  for (i = 0; i < sideLength; i++) {
    var tmp = [];
    for (j = 0; j < sideLength; j++) {
      tmp.push(sentence[sideLength * i + j]);
    }
    data.push(tmp);
  }

  // 表の動的作成
  makeTable(data, "q1div");
  // 色を初期化
  color_reset();

  // サイズの変更
  setSize();
})

$(window).resize(setSize)

function setSize() {
  // 基本となるサイズの取得
  const size = $('body').outerWidth() * 0.6;

  // 天使のサイズ
  $('#engelimg').height(Math.min($('#engelballoon').width() * 0.4, 200))

  // 解答欄のサイズ
  $('.ans_box').css({ 'font-size': $('#q1').width() * 0.08 });
  $('.ans_box').width($('#q1').width() * 0.12);
  $('.ans_box').height($('#q1').width() * 0.12);
  $('.ans_box_deco').css({ 'font-size': $('#q1').width() * 0.08 });
  $('.ans_box_deco').width($('#q1').width() * 0.12);
  $('.ans_box_deco').height($('#q1').width() * 0.1);

  // 問題1の設定
  $('.q1_btn').css({ 'font-size': $('#q1').width() * 0.06 });

  // 問題2の設定
  const q2Size = $('#q2').width();
  $('.q2areadiv').width(q2Size * 0.84);
  $('.q2areadiv').height(q2Size * 0.6);
  $('.q2contents').width(q2Size * 0.09);
  $('.q2contents').height(q2Size * 0.3);
  $('.q2contents').css({ 'font-size': q2Size * 0.085 });
}