// メニューボタン取得
const RepostMenuBtn = document.getElementById('repost-button');
// ポップアップメニュー取得
const RepostMenu = document.getElementById('repostmenu');
// クローズボタン取得
const RepostMenuClose = document.getElementById('repost-menu-close');

MenuBtn.addEventListener("click", () => {
    repostmenuOpen("open");
  });
  
  function repostmenuOpen(mode) {
    if (mode === "open") {
      RepostMenu.style.display = "block";
    }
  }

RepostMenuClose.addEventListener("click", () => {
    repostmenuClose("close");
  });

  function repostmenuClose(mode) {
    if (mode === "close") {
    RepostMenu.style.display = "none";
    }
}

  addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == PopMenu) {
    RepostMenu.style.display = "none";
  }
}
