firebase.auth().onAuthStateChanged((user) => {
    if (user) {
       // Preenche o nome e email do formulário
       $('#name').val(user.displayName);
       $('#email').val(user.email);
    } else {
        $('#name').val('');
       $('#email').val('');
    }
});