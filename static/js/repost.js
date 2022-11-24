
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
