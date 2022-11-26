// メニューボタン取得
const MenuBtn = document.getElementById('menu-btn');
// ポップアップメニュー取得
const PopMenu = document.getElementById('pop-menu');
// クローズボタン取得
const MenuClose = document.getElementById('menu-close');

MenuBtn.addEventListener("click", () => {
    menuOpen("open");
  });
  
  function menuOpen(mode) {
    if (mode === "open") {
      PopMenu.style.display = "block";
    }
  }

MenuClose.addEventListener("click", () => {
    menuClose("close");
  });

  function menuClose(mode) {
    if (mode === "close") {
    PopMenu.style.display = "none";
    }
}

  addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == PopMenu) {
    PopMenu.style.display = "none";
  }
}
