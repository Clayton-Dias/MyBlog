// Monitora mudanças no estado de autenticação do usuário
firebase.auth().onAuthStateChanged((user) => {
    // Verifica se um usuário está logado
    if (user) {
        // Se o usuário estiver logado, oculta a seção de login
        $('#makeLogin').hide();

        // Preenche os campos de nome e e-mail com os dados do usuário logado
        $('#commentName').val(user.displayName); // Define o nome do usuário no campo de comentário
        $('#commentEmail').val(user.email); // Define o e-mail do usuário no campo de comentário

        // Mostra o formulário de comentário
        $('#commentForm').show(); // Exibe o formulário para que o usuário possa fazer um comentário
    } else {
        // Se não houver um usuário logado, oculta o formulário de comentário
        $('#commentForm').hide(); // Esconde o formulário de comentário

        // Limpa os campos de nome e e-mail, já que não há um usuário logado
        $('#commentName').val(''); // Limpa o campo de nome
        $('#commentEmail').val(''); // Limpa o campo de e-mail

        // Mostra a seção de login novamente
        $('#makeLogin').show(); // Exibe a opção de login para o usuário
    }
});
