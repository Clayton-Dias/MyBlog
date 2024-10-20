// Monitora mudanças no estado de autenticação do usuário
firebase.auth().onAuthStateChanged((user) => {
    // Verifica se um usuário está logado
    if (user) {
        // Se o usuário estiver logado, preenche os campos do formulário com os dados do usuário
        $('#name').val(user.displayName); // Preenche o campo 'name' com o nome do usuário
        $('#email').val(user.email); // Preenche o campo 'email' com o e-mail do usuário
    } else {
        // Se não houver um usuário logado, limpa os campos do formulário
        $('#name').val(''); // Limpa o campo 'name'
        $('#email').val(''); // Limpa o campo 'email'
    }
});
