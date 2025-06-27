<?php

$tokenFile = __DIR__ . '/token.json';

$client_id = '229a4c5c4e14984efae60fab87aa2bdd';
$client_secret = 'xMCjUiWwI6o33b+A7QaoU2OhKkfhLUv8hsMXG6s78Qw=';
$token_url = 'http://localhost/peoplesuite-ohrmv5/web/index.php/oauth2/token';

function loadTokens($tokenFile) {
    return json_decode(file_get_contents($tokenFile), true);
}

function saveTokens($tokenFile, $tokens) {
    file_put_contents($tokenFile, json_encode($tokens, JSON_PRETTY_PRINT));
}

function refreshAccessToken($refresh_token, $client_id, $client_secret, $token_url) {
    $postData = [
        'grant_type' => 'refresh_token',
        'refresh_token' => $refresh_token,
        'client_id' => $client_id,
        'client_secret' => $client_secret
    ];

    $ch = curl_init($token_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        die("Curl error: " . curl_error($ch));
    }
    curl_close($ch);

    return json_decode($response, true);
}

$tokens = loadTokens($tokenFile);
$newTokens = refreshAccessToken($tokens['refresh_token'], $client_id, $client_secret, $token_url);

if (isset($newTokens['access_token'])) {
    saveTokens($tokenFile, $newTokens);
    echo "Access token refreshed successfully.\n";
    # === DISPLAY TO CONSOLE ===
    echo file_get_contents($tokenFile);
    file_put_contents(__DIR__ . '/refresh_log.txt', date('Y-m-d H:i:s') . " - Token refreshed\n", FILE_APPEND);
} else {
    echo "Failed to refresh token: " . json_encode($newTokens) . "\n";
}