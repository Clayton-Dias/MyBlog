/** Conexão ao Firebase **/

// Dados para conexão com o Firebase 
const firebaseConfig = {
    apiKey: "XXXXXXXXXXXXXXYYYYYYYYYY",
    authDomain: "myblog-flask.firebaseapp.com",
    projectId: "myblog-flask",
    storageBucket: "myblog-flask.appspot.com",
    messagingSenderId: "534410500699",
    appId: "1:534410500699:web:1352e94e2126ba8cee7d7e"
};

// Conexão com o Firebase, usando o dados para conexão
const app = firebase.initializeApp(firebaseConfig);

// Seleciona o provedor de autenticação → Google (neste caso)
var provider = new firebase.auth.GoogleAuthProvider();


firebase.auth().onAuthStateChanged((user) => {
    if (user) {
        // Troca a ação do botão para 'profile'
        $('#loginUserr').attr({'data-action': 'profile'})
        $('#loginUser img').attr({
            'src': user.photoURL,
            'alt': user.displayName
        })
    } else {
        // Troca a ação do botão para 'login'
        $('#loginUserr').attr({ 'data-action': 'login' })
        // Troca para a imagem do usuário
        $('#loginUser img').attr({
            'src': '/static/img/user.png',
            'alt': 'Logue-se'
        })
    }
});

// Login
function login() {
    // Faz login pelo Google usando popup
    firebase.auth().signInWithPopup(provider);
};

// logout
function logout() {
    firebase.auth().signOut();
}

// Excluir conta do uduário
function userRemove() {
    const user = firebase.auth().currentUser;
    user.delete();
}


// Inicializa jQuery
$(document).ready(myApp);

// Aplicativo Principal
function myApp() {
    //Monitora cliques no botão de login/logout
    $('#loginUser').click(userToggle);
}


//Login/Logout do usuário
function userToggle() {

    // Lê o atributo 'data-action' do elemento '#btnUser'
    if ($('#loginUser').attr('data-action') == 'login') {
        //executa o login
        login()
    } else {
        // Temporário: faz logout
        // logout();
        
        // Mostra o perfil do usuári
        location.href = '/profile';
    }

}
