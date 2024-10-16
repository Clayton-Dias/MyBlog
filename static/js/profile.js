$(document).ready(runProfile)


firebase.auth().onAuthStateChanged((user) => {
    // Se ususário está logado
    if (user) {
        $('logged img').attr({
            'src': user.photoURL,
            'alt': user.displayName
        });

        $('logged h4').html(user.displayName);

        $('#id').html('ID: ' + user.uid);

        $('#email').attr('E-mail: ' + user.email);

        $('#registered').html('Cadastrado em ' + dateConvert(user.metadata.creationTime));

        $('#lastLogin').html('ùltimo login em ' + dateConvert(user.metadata.lastSignInTime));

        $('#notLogged').hide();

        $('#logged').show();


    } else {

        $('#logged').hide();

        $('#notLogged').show();

       
    }
});


function dateConvert(date) {
    // Cria um novo objeto Date a partir do argumento fornecido.
    const date = new Date(date);

    // Obtém o dia do mês (1-31) e o converte para uma string com dois dígitos.
    const day = date.getDate().toString().padStart(2, '0');

    // Obtém o mês (0-11), adiciona 1 para ajustar ao formato (1-12), e o converte para uma string com dois dígitos.
    const month = (date.getMonth() + 1).toString().padStart(2, '0');

    // Obtém o ano completo (ex: 2024).
    const year = date.getFullYear();

    // Formata a data no formato 'dd/mm/aaaa'.
    const formattedDate = `${day}/${month}/${year}`;

    // Retorna a data formatada.
    return formattedDate;
}

function runProfile() {
    $('#toGoogle').click(() => {
        window.open('https://myaccount.google.com/', '_blank');
    })

    $('#btnLogout').click(logout);


    $('#btnLogin').click(login);
}

/***
 *  Código do professor
 * 
 * $(document).ready(runProfile)

firebase.auth().onAuthStateChanged((user) => {
    // Se ususário está logado
    if (user) {
        $('#logged img').attr({
            'src': user.photoURL,
            'alt': user.displayName
        })
        $('#logged h4').html(user.displayName)
        $('#id').html('ID: ' + user.uid)
        $('#email').html('E-mail: ' + user.email)
        $('#registered').html('Cadastrado em ' + dateConvert(user.metadata.creationTime))
        $('#lastLogin').html('Último login em ' + dateConvert(user.metadata.lastSignInTime))
        $('#notLogged').hide()
        $('#logged').show()
    } else {
        $('#logged').hide()
        $('#notLogged').show()
    }
});

function runProfile() {
    // Mostra o perfil do usuário no Google
    $('#toGoogle').click(() => {
        window.open('https://myaccount.google.com/', '_blank');
    })

    // Faz logout 
    $('#btnLogout').click(logout);

    // Faz login
    $('#btnLogin').click(login);
}


function dateConvert(date) {
    // Cria uma nova instância do objeto Date com base no valor de date
    const dateObj = new Date(date);

    // Obtém o dia do mês e adiciona um zero à esquerda caso tenha um dígito
    const day = dateObj.getDate().toString().padStart(2, '0');

    // Obtém o mês (0-11), adiciona 1 para ajustar ao formato humano (1-12) e adiciona um zero à esquerda
    const month = (dateObj.getMonth() + 1).toString().padStart(2, '0');

    // Obtém o ano completo
    const year = dateObj.getFullYear();

    // Formata a data como dd/mm/yyyy
    const formattedDate = `${day}/${month}/${year}`;

    // Retorna a data formatada
    return formattedDate;
}**/