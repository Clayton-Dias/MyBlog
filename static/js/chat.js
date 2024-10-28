$(document).ready(function () {
    $('#chat-icon').click(function () {
        $('#chat-box').toggle(); // Mostra ou esconde o chat
    });

    $('#close-chat').click(function () {
        $('#chat-box').hide(); // Fecha o chat
    });

    $('#send-message').click(function () {
        let message = $('#chat-input').val();
        if (message) {
            $('#chat-messages').append(`<div><strong>Você:</strong> ${message}</div>`);
            $('#chat-input').val(''); // Limpa o input

            // Envia a mensagem para o servidor Flask
            $.ajax({
                type: 'POST',
                url: '/chat',
                contentType: 'application/json',
                data: JSON.stringify({ message: message }),
                success: function (response) {
                    $('#chat-messages').append(`<div><strong>Gemini:</strong> ${response.reply}</div>`);
                }

            });
        }
        return false;
    });
});
