// モーダルを表示させる
const repostChannelModal = document.getElementById("repost-message-modal");
// モーダルを開く
const repostChannelOpen = document.getElementById("repost-page-open-btn");
// モーダルを閉じる
const repostChannelClose = document.getElementById("repost-page-close-btn");

// モーダルを開く
repostChannelOpen.addEventListener("click", modalOpen);
function modalOpen() {
  repostChannelModal.style.display = "block";
}

// ×印がクリックされたとき
repostChannelClose.addEventListener("click", modalClose);
function modalClose() {
  repostChannelModal.style.display = "none";
}




// モーダルコンテンツ以外がクリックされたとき

addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == repostChannelModal) {
    repostChannelModal.style.display = "none";
  }
}

/*
const repostChannel = () => {
    if (uid !== channel.uid) {
        return;
      } else {
        modalOpen("repost");
      }
};
*/

