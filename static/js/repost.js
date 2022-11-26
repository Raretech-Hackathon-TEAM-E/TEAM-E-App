//repost
const repostModal = document.getElementById("repost-message-modal");
// モーダルを開くボタン取得
const repostBtn = document.getElementById("repost-button");
// モーダルクローズボタン取得
const repostPageButtonClose = document.getElementById("repost-page-close-btn");


const repostMessage = () => {
  if (uid !== message.uid) {
    return;
  } else {
    modalOpen("repost");
  }
};


function modalOpen(mode) {
  if (mode === "repost") {
    repostModal.style.display = "block";
  }
}


repostBtn.addEventListener("click", repostMessage);


// モーダル内のバツ印がクリックされた時

repostPageButtonClose.addEventListener("click", () => {
  modalClose("repost")
});

function modalClose(mode) {
  if (mode === "repost") {
    repostModal.style.display = "none";
  }
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == repostModal) {
    repostModal.style.display = "none";
  }
}
