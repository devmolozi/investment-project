function validar() {
    var senha = formuser.senha.value;
    var rep_senha = formuser.rep_senha.value;

    if (senha == "" || senha.lenght <= 5) {
        alert('Preencha o campo de senha com no minimo 5 caracteres');
        formuser.senha.focus();
        return false;
    }

    if (rep_senha == "" || rep_senha.lenght <= 5) {
        alert('Preencha o campo de senha com no minimo 5 caracteres');
        formuser.senha.focus();
        return false;
    }

    if (senha != rep_senha) {
        alert("Senhas diferentes");
        form1.rep_senha.focus();
        return false
    }
}