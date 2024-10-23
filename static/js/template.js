/** Conexão ao Firebase **/

// Dados para conexão com o Firebase 
const firebaseConfig = {
    apiKey: "", // Chave da API
    authDomain: "myblog-flask.firebaseapp.com", // Domínio de autenticação
    projectId: "myblog-flask", // ID do projeto
    storageBucket: "myblog-flask.appspot.com", // Bucket de armazenamento
    messagingSenderId: "534410500699", // ID do remetente de mensagens
    appId: "1:534410500699:web:1352e94e2126ba8cee7d7e" // ID do aplicativo
};

// Conexão com o Firebase, usando os dados de configuração
const app = firebase.initializeApp(firebaseConfig);

// Seleciona o provedor de autenticação → Google
var provider = new firebase.auth.GoogleAuthProvider();

// Monitora mudanças no estado de autenticação do usuário
firebase.auth().onAuthStateChanged((user) => {
    if (user) {
        // Se o usuário estiver logado, atualiza o botão para a ação 'profile'
        $('#loginUserr').attr({ 'data-action': 'profile' });

        // Atualiza a imagem do usuário logado
        $('#loginUser img').attr({
            'src': user.photoURL, // URL da foto do perfil do usuário
            'alt': user.displayName // Nome de exibição do usuário como texto alternativo
        });
    } else {
        // Se não houver usuário logado, atualiza o botão para a ação 'login'
        $('#loginUserr').attr({ 'data-action': 'login' });

        // Define a imagem padrão para usuários não logados
        $('#loginUser img').attr({
            'src': '/static/img/user.png', // Imagem padrão quando não está logado
            'alt': 'Logue-se' // Texto alternativo padrão
        });
    }
});


// Função para login do usuário
function login() {
    // Faz login pelo Google usando um popup
    firebase.auth().signInWithPopup(provider);
}

// Função para logout do usuário
function logout() {
    firebase.auth().signOut(); // Desconecta o usuário
}

// Função para excluir a conta do usuário
function userRemove() {
    const user = firebase.auth().currentUser; // Obtém o usuário atual
    user.delete(); // Exclui a conta do usuário logado
}

// Inicializa jQuery e configura o aplicativo principal
$(document).ready(myApp);

// Função principal do aplicativo
function myApp() {
    // Monitora cliques no botão de login/logout
    $('#loginUser').click(userToggle);
}

// Função para alternar entre login e logout do usuário
function userToggle() {
    // Lê o atributo 'data-action' do elemento '#loginUser'
    if ($('#loginUser').attr('data-action') == 'login') {
        // Se o atributo for 'login', executa o login
        login();
    } else {
        // Caso contrário, redireciona para o perfil do usuário
        // Temporário: faz logout
        // logout(); // (comentado por enquanto)

        // Redireciona para a página de perfil
        location.href = '/profile';
    }
}

