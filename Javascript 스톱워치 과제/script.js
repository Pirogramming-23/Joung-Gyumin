const display = document.getElementById("display");
const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");
const resetBtn = document.getElementById("reset");
const selectAll = document.getElementById("selectAll");
const deleteSelected = document.getElementById("deleteSelected");
const lapList = document.getElementById("lapList");

let startTime = 0;
let elapsedTime = 0;
let timerInterval = null;

function formatTime(ms) {
    const seconds = String(Math.floor(ms / 1000)).padStart(2, '0');
    const centiseconds = String(Math.floor((ms % 1000) / 10)).padStart(2, '0');
    return `${seconds} : ${centiseconds}`;
}

// start
startBtn.addEventListener("click", () => {
    if (timerInterval) return; // 중복 실행 방지

    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        display.textContent = formatTime(elapsedTime);
    }, 10);
});

// stop
stopBtn.addEventListener("click", () => {
    clearInterval(timerInterval);
    timerInterval = null;
    recordLap(display.textContent);
});

// reset
resetBtn.addEventListener("click", () => {
    clearInterval(timerInterval);
    timerInterval = null;
    elapsedTime = 0;
    display.textContent = "00 : 00";
});

// 구간 기록
function recordLap(timeText) {
    const li = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    const timeSpan = document.createElement("span");
    timeSpan.textContent = timeText;

    li.appendChild(checkbox);
    li.appendChild(timeSpan);
    lapList.appendChild(li);
}

// 전체 선택
selectAll.addEventListener("change", function () {
    const checkboxes = document.querySelectorAll("#lapList input[type='checkbox']");
    checkboxes.forEach(cb => cb.checked = this.checked);
});

// 각 항목 체크 → 전체선택 동기화
lapList.addEventListener("change", () => {
    const checkboxes = lapList.querySelectorAll("input[type='checkbox']");
    const allChecked = [...checkboxes].every(cb => cb.checked);
    selectAll.checked = allChecked;
});

// 선택 삭제
deleteSelected.addEventListener("click", () => {
    const checkedItems = lapList.querySelectorAll("input[type='checkbox']:checked");
    checkedItems.forEach(cb => cb.closest("li").remove());
});
