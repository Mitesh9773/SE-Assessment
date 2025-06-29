#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()

using namespace std;

// Class
class RockPaperScissors
{
private:
    string playerName;
    int rounds;
    int playerScore;
    int computerScore;

public:
    // Constructor
    RockPaperScissors(string name, int totalRounds)
    {
        playerName = name;
        rounds = totalRounds;
        playerScore = 0;
        computerScore = 0;
    }

    // Function to display menu
    void displayMenu()
    {
        cout << "\nChoose your move:\n";
        cout << "1. Rock\n";
        cout << "2. Paper\n";
        cout << "3. Scissors\n";
        cout << "Enter your choice: ";
    }

    // Function to play the game
    void playGame()
    {
        srand(time(0)); // Seed for random number generation

        for (int round = 1; round <= rounds; round++)
        {
            cout << "\n      Round: " << round << "      \n";

            int playerChoice, computerChoice;

            displayMenu();
            cin >> playerChoice;

            if (playerChoice < 1 || playerChoice > 3)
            {
                cout << "Invalid choice! Round skipped.\n";
                continue;
            }

            computerChoice = (rand() % 3) + 1;

            // Display choices
            cout << playerName << " chose: " << getChoiceName(playerChoice) << endl;
            cout << "Computer chose: " << getChoiceName(computerChoice) << endl;

            if (playerChoice == computerChoice)
            {
                cout << "Result: It's a Tie!\n";
            }
            else if ((playerChoice == 1 && computerChoice == 3) ||
                     (playerChoice == 2 && computerChoice == 1) ||
                     (playerChoice == 3 && computerChoice == 2))
            {
                cout << "Result: " << playerName << " Wins!\n";
                playerScore++;
            }
            else
            {
                cout << "Result: Computer Wins!\n";
                computerScore++;
            }
        }

        // Display final result
        displayResult();
    }

    // Function to convert choice number to string
    string getChoiceName(int choice)
    {
        switch (choice)
        {
        case 1:
            return "Rock";
        case 2:
            return "Paper";
        case 3:
            return "Scissors";
        default:
            return "Unknown";
        }
    }

    // Function to display final results
    void displayResult()
    {
        cout << "\n        Final Result        \n";
        cout << playerName << "'s Score: " << playerScore << endl;
        cout << "Computer's Score: " << computerScore << endl;

        if (playerScore > computerScore)
        {
            cout << "Congratulations " << playerName << ", You Won the Game!\n";
        }
        else if (computerScore > playerScore)
        {
            cout << "Computer Wins the Game. Better luck next time!\n";
        }
        else
        {
            cout << "The Game is a Tie!\n";
        }
    }
};

int main()
{
    string name;
    int totalRounds;

    cout << "       Welcome to Rock Paper Scissors Game      \n";
    cout << "Enter your name: ";
    getline(cin, name);

    cout << "Enter the number of rounds you want to play: ";
    cin >> totalRounds;

    // Create object of class
    RockPaperScissors game(name, totalRounds);

    // Start the game
    game.playGame();

    cout << "\n      Thank you for playing!     \n";
    return 0;
}
