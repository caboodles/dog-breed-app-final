document.getElementById("fileInput").addEventListener("change", function (e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (event) {
            const imgElement = document.getElementById("imagePreview");
            imgElement.src = event.target.result;
            imgElement.style.display = "block";
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById("uploadForm").addEventListener("submit", function (e) {
    e.preventDefault();
    let formData = new FormData();
    let fileInput = document.getElementById("fileInput");
    if (fileInput.files.length > 0) {
        formData.append("file", fileInput.files[0]);
        fetch("http://localhost:5000/upload", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.breed) {
                    document.getElementById("breedLabel").innerText = "견종 :";
                    document.getElementById("breedName").innerText = data.breed;
                    document.getElementById("infoLabel").innerText = "정보:";
                    document.getElementById("breedInfo").innerText = data.info;
                } else if (data.error) {
                    document.getElementById(
                        "breedInfo"
                    ).innerText = `Error: ${data.error}`;
                }
            })
            .catch((error) => console.error("Error:", error));
    } else {
        alert("업로드할 파일을 선택해주세요.");
    }
});
