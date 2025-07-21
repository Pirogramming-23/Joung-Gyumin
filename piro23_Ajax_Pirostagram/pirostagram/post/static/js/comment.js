// function addComment(event, postId) {
//   event.preventDefault(); // 폼 submit 방지

//   const form = event.target;
//   const contentInput = form.querySelector('input[name="content"]');
//   const content = contentInput.value.trim();

//   if (!content) return;

//   axios.post(`/add_comment_ajax/${postId}/`, {
//     content: content
//   }, {
//     headers: {
//       'X-CSRFToken': getCookie('csrftoken')
//     }
//   })
//   .then(response => {
//     if (response.data.success) {
//       const newComment = document.createElement('li');
//       newComment.className = 'comment-item';
//       newComment.innerHTML = `
//         <div class="comment-left">
//           <strong>${response.data.author}</strong> ${response.data.content}
//         </div>
//         <button onclick="deleteComment(${response.data.comment_id})"
//                 id="comment-del-${response.data.comment_id}"
//                 class="delete-button">
//           삭제
//         </button>
//       `;

//       const ul = form.closest('.feed-wrapper').querySelector('.comment-section ul');
//       ul.appendChild(newComment);

//       contentInput.value = ''; // 입력창 초기화
//     }
//   })
//   .catch(error => {
//     console.error('댓글 등록 실패:', error);
//     alert('댓글 등록 중 오류가 발생했습니다.');
//   });
// }

// function deleteComment(commentId) {
//   if (!confirm('정말 삭제하시겠습니까?')) return;

//   axios.post(`/comment/delete-ajax/${commentId}/`, {}, {
//     headers: {
//       'X-CSRFToken': getCookie('csrftoken')
//     }
//   })
//   .then(response => {
//     if (response.data.success) {
//       const btn = document.getElementById(`comment-del-${commentId}`);
//       const li = btn.closest('li');
//       li.remove();
//     }
//   })
//   .catch(error => {
//     console.error('삭제 실패:', error);
//     alert('삭제 중 오류가 발생했습니다.');
//   });
// }
function addComment(event, postId) {
  event.preventDefault();

  const form = event.target;
  const contentInput = form.querySelector('input[name="content"]');
  const content = contentInput.value.trim();

  if (!content) return;

  axios.post(`/add_comment_ajax/${postId}/`, {
    content: content
  }, {
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  })
  .then(response => {
    if (response.data.success) {
      const newComment = document.createElement('li');
      newComment.className = 'comment-item';
      newComment.innerHTML = `
        <div class="comment-left">
          <strong>${response.data.author}</strong> ${response.data.content}
        </div>
        <button 
          class="delete-button" 
          data-comment-id="${response.data.id}">
          삭제
        </button>
      `;

      const ul = form.closest('.feed-wrapper').querySelector('.comment-section ul');
      ul.appendChild(newComment);

      contentInput.value = '';
    }
  })
  .catch(error => {
    console.error('댓글 등록 실패:', error);
    alert('댓글 등록 중 오류가 발생했습니다.');
  });
}

document.addEventListener('click', function(event) {
  if (event.target.classList.contains('delete-button')) {
    const commentId = event.target.dataset.commentId;

    if (!commentId || !confirm('정말 삭제하시겠습니까?')) return;

    axios.post(`/comment/delete-ajax/${commentId}/`, {}, {
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    })
    .then(response => {
      if (response.data.success) {
        const li = event.target.closest('li');
        li.remove();
      } else {
        alert('삭제 권한이 없습니다.');
      }
    })
    .catch(error => {
      console.error('삭제 실패:', error);
      alert('삭제 중 오류가 발생했습니다.');
    });
  }
});