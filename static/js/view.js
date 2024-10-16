firebase.auth().onAuthStateChanged((user) => {
    if (user) {

        // Oculta o login
        $('#makeLogin').hide();

        //Preenche os campos nome e email com os dados do login do usuário
        $('#commentName').val(user.displayName);
        $('#commentEmail').val(user.email);

        // Mostra o formulário de comentário
        $('#commentForm').show();
    } else {
        // Oculta o formulário de comentário
        $('#commentForm').hide();

        //Limpar os campos nome e email com os dados do login do usuário
        $('#commentName').val('');
        $('#commentEmail').val('');


        // Oculta o login
        $('#makeLogin').show();
    }
});