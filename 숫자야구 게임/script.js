let answer = [];
let attempts = 9;

function generateAnswer() {
    const digits = [0,1,2,3,4,5,6,7,8,9];
    answer = [];
    while (answer.length < 3) {
        const idx = Math.floor(Math.random() * digits.length);
        answer.push(digits.splice(idx, 1)[0]);
    }
}

function initializeGame() {
    generateAnswer();  
    attempts = 9;      

    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';
    document.getElementById("number3").value = '';
    document.getElementById("results").innerHTML = '';

    const img = document.getElementById("game-result-img");
    img.src = '';
    img.alt = '';

    document.getElementById("attempts").textContent = attempts;
    document.querySelector(".submit-button").disabled = false;
}
function resetInputs() {
    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';
    document.getElementById("number3").value = '';
    document.getElementById("number1").focus();
}

function check_numbers() {
    const num1 = document.getElementById("number1").value;
    const num2 = document.getElementById("number2").value;
    const num3 = document.getElementById("number3").value;

    if (!num1 || !num2 || !num3) {
        resetInputs();
        return;
    }

    const guess = [Number(num1), Number(num2), Number(num3)];

    if (new Set(guess).size !== guess.length) {
        alert("서로 다른 숫자 3개를 입력해주세요!");
        resetInputs();
        return;
    }

    attempts--;
    document.getElementById("attempts").textContent = attempts;

    let strike = 0;
    let ball = 0;

    for (let i = 0; i < 3; i++) {
        if (guess[i] === answer[i]) {
            strike++;
        } else if (answer.includes(guess[i])) {
            ball++;
        }
    }
    const resultDiv = document.getElementById("results");
    const row = document.createElement("div");
    row.classList.add("check-result");

    const left = document.createElement("div");
    left.classList.add("left");
    left.innerText = guess.join(" ");
    row.appendChild(left);

    const right = document.createElement("div");
    right.classList.add("right");
    
    if (strike === 0 && ball === 0) {
        const out = document.createElement("span");
        out.innerText = "O";
        out.classList.add("num-result", "out");
        right.appendChild(out);
    } else {
        const sNum = document.createTextNode(`${strike}`);
        const s = document.createElement("span");
        s.innerText = "S";
        s.classList.add("num-result", "strike");
        s.style.marginLeft = "6px";

        const bNum = document.createTextNode(`${ball}`);
        const b = document.createElement("span");
        b.innerText = "B";
        b.classList.add("num-result", "ball");
        b.style.marginLeft = "6px";

        right.appendChild(sNum);
        right.appendChild(s);
        right.appendChild(document.createTextNode(" "));
        right.appendChild(bNum);
        right.appendChild(b);
    }

    const colon = document.createElement("div");
    colon.innerText = " : ";
    colon.style.fontWeight = "bold";
    colon.style.margin = "0px 90px";
    row.style.justifyContent = "space-between";
    row.style.display = "flex"; 

    row.appendChild(colon);

    row.appendChild(right);
    resultDiv.appendChild(row);


    if (strike === 3) {
        endGame(true); 
    } else if (attempts === 0) {
        endGame(false); 
    }

    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';
    document.getElementById("number3").value = '';
    document.getElementById("number1").focus();
}

function endGame(isWin) {
    const img = document.getElementById("game-result-img");

    if (isWin) {
        img.src = "success.png";
        img.alt = "승리";

    } else {
        img.src = "fail.png";
        img.alt = "패배";

        const reveal = document.createElement("div");
        reveal.style.marginTop = "8px";
        reveal.style.fontWeight = "bold";
        reveal.innerText = `정답: ${answer.join(" ")}`;
        document.getElementById("results").appendChild(reveal);
    }

    document.querySelector(".submit-button").disabled = true;
    document.getElementById("number1").disabled = true;
    document.getElementById("number2").disabled = true;
    document.getElementById("number3").disabled = true;

}

window.onload = () => {
    initializeGame();

    const inputs = [
        document.getElementById("number1"),
        document.getElementById("number2"),
        document.getElementById("number3")
    ];

    for (let input of inputs) {
        input.addEventListener("input", function () {
            const val = input.value;

            // 숫자 0~9 외 입력 제한
            if (!/^[0-9]?$/.test(val)) {
                alert("숫자 0~9 사이의 숫자를 입력해주세요!");
                input.value = '';
                return;
            }

            // 중복 입력 확인
            for (let otherInput of inputs) {
                if (otherInput !== input && otherInput.value === val && val !== '') {
                    alert("서로 다른 숫자를 입력해주세요!");
                    input.value = '';
                    return;
                }
            }
        });
    }
};
