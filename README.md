Flet for the UI and game mechanics (flipping cards, managing turns, timers, and scores).
User Invitations through unique secret IDs for multiplayer.
Turn-based gameplay where each player gets 5 seconds to make a move.
Paging System so users can invite others to play.
Nodemailer to send notifications when a player is invited.

Plan for Development
1. Multiplayer Game Logic

    Players take turns flipping cards.
    5-second countdown per turn.
    Score is updated based on successful matches.

2. Game Invitation System

    Each player has a unique secret ID.
    Players can invite others via a UI prompt.
    Once invited, the recipient gets an email with a game link.

3. Real-time Gameplay

    Use WebSockets for real-time updates when a move is made.
    Show an alert when the other player plays their turn.
