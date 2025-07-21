function toggleLike(postId) {
  axios.post(`/like-ajax/${postId}/`, {}, {
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  })
  .then(response => {
    const icon = document.getElementById(`like-icon-${postId}`);
    const count = document.getElementById(`like-count-${postId}`);

    if (response.data.liked) {
      icon.innerHTML = `
        <svg width="24" height="24" fill="black" stroke="black" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
        </svg>`;
    } else {
      icon.innerHTML = `
        <svg width="24" height="24" fill="none" stroke="black" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
        </svg>`;
    }

    count.innerText = `좋아요 ${response.data.like_count}개`;
  })
  .catch(error => {
    console.error(error);
  });
}




// CSRF 쿠키 가져오기
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
