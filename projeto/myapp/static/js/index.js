// Calculando dias para o fim do mes

let diasDoMes = document.getElementById("fimDoMes");
Date.prototype.fimDoMes = function () {
    var days = [30, 31],
        m = this.getMonth();

    if (m == 1) {
        return this.getFullYear() % 4 == 0 &&
            (this.getFullYear() % 100 != 0 || this.getFullYear() % 400 == 0)
            ? 29
            : 28;
    } else {
        return days[(m + (m < 7 ? 1 : 0)) % 2];
    }
};

var myDate = new Date();
var diasCorridos = myDate.getDate();
let diasParaFimDomMes = myDate.fimDoMes() - diasCorridos;
if (diasDoMes) {
    diasDoMes.innerText = diasParaFimDomMes;
}

// Calculando meta do dia
let meta = document.getElementById("meta");
let vendido = document.getElementById("vendido");
let faltaParaBaterMeta = document.getElementById("faltaParaMeta");

if (meta) {
    var faltaParaMeta = Number(meta.textContent) - Number(vendido.textContent);
}

let metaDoDia = document.getElementById("metaDoDia");
if (metaDoDia) {
    metaDoDia.innerText = (faltaParaMeta / Number(diasParaFimDomMes)).toFixed(
        2
    );
}

if (faltaParaBaterMeta) {
    faltaParaBaterMeta.innerText = faltaParaMeta
}


// Formatação de formulário para adicionar venda
let addVenda = document.getElementById("addVenda");
let addVendaForm = document.getElementById("addVendaForm");

let editMeta = document.getElementById("editMeta");
let editMetaForm = document.getElementById("editMetaForm");

let cancelVenda = document.getElementById("cancelVenda");
let cancelVendaHr = document.getElementById("cancelVendaHr");

let cancelEditMeta = document.getElementById("cancelEditMeta");
let cancelEditMetaHr = document.getElementById("cancelEditMetaHr");

if (addVenda) {
    addVenda.addEventListener("click", () => {
        addVendaForm.style.display = "flex";
        cancelVenda.style.display = "flex";
        cancelVendaHr.style.display = "flex";
    });
}

if (cancelVenda) {
    cancelVenda.addEventListener("click", () => {
        addVendaForm.style.display = "none";
        cancelVenda.style.display = "none";
        cancelVendaHr.style.display = "none";
    });
}

if (editMeta) {
    editMeta.addEventListener("click", () => {
        editMetaForm.style.display = "flex";
        cancelEditMeta.style.display = "flex";
        cancelEditMetaHr.style.display = "flex";
    });
}

if (cancelEditMeta) {
    cancelEditMeta.addEventListener("click", () => {
        editMetaForm.style.display = "none";
        cancelEditMeta.style.display = "none";
        cancelEditMetaHr.style.display = "none";
    });
}