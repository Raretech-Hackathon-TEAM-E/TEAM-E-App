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

/*
// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", modalOpen);
function modalOpen() {
  addChannelModal.style.display = "block";
}


deleteChannelBtn.addEventListener("click", modalOpen);
function modalOpen() {
  deleteChannelModal.style.display = "block";
}
*/


// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == repostModal) {
    repostModal.style.display = "none";
  }
}

/*
function repostsubmit() {
    if(uid !== item.uid) {
        return
    } else if (uid === item.uid) {
      const repostButtonLink = document.getElementById("repost-link");
      const repostButton = document.getElementById("repost-btn");
      const url = `/repost/${item.mid}`;
      repostButtonLink.setAttribute("href", url);
      repostButton.setAttribute("type", submit);
  };
}
*/