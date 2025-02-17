#include <iostream>
#include <vector>
#include <fstream>
#include <map>

using namespace std;

// Playfair Cipher Implementation
class PlayfairCipher {
private:
    char matrix[6][6];
    map<char, pair<int, int>> position;

    void generateMatrix(string key) {
        string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        string newKey = "";
        map<char, bool> used;

        for (char c : key) {
            if (!used[c] && alphabet.find(c) != string::npos) {
                newKey += c;
                used[c] = true;
            }
        }
        for (char c : alphabet) {
            if (!used[c]) {
                newKey += c;
            }
        }

        int index = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                matrix[i][j] = newKey[index];
                position[newKey[index]] = {i, j};
                index++;
            }
        }
    }

public:
    PlayfairCipher(string key) {
        generateMatrix(key);
    }

    string encrypt(string text) {
        string encrypted = "";
        for (size_t i = 0; i < text.size(); i += 2) {
            char a = text[i], b = (i + 1 < text.size()) ? text[i + 1] : 'X';
            int r1 = position[a].first, c1 = position[a].second;
            int r2 = position[b].first, c2 = position[b].second;

            if (r1 == r2) {
                encrypted += matrix[r1][(c1 + 1) % 6];
                encrypted += matrix[r2][(c2 + 1) % 6];
            } else if (c1 == c2) {
                encrypted += matrix[(r1 + 1) % 6][c1];
                encrypted += matrix[(r2 + 1) % 6][c2];
            } else {
                encrypted += matrix[r1][c2];
                encrypted += matrix[r2][c1];
            }
        }
        return encrypted;
    }
};

// Hill Cipher Implementation
class HillCipher {
private:
    vector<vector<int>> keyMatrix;
    int modInverse(int a, int m) {
        for (int x = 1; x < m; x++) {
            if ((a * x) % m == 1)
                return x;
        }
        return -1;
    }

public:
    HillCipher(vector<vector<int>> key) : keyMatrix(key) {}
    
    string encrypt(string text) {
        while (text.length() % 3 != 0) text += 'X';
        string encrypted = "";
        
        for (size_t i = 0; i < text.size(); i += 3) {
            vector<int> block(3);
            for (int j = 0; j < 3; j++)
                block[j] = text[i + j] - 'A';

            vector<int> result(3, 0);
            for (int row = 0; row < 3; row++)
                for (int col = 0; col < 3; col++)
                    result[row] += keyMatrix[row][col] * block[col];
            
            for (int j = 0; j < 3; j++)
                encrypted += (char)((result[j] % 26) + 'A');
        }
        return encrypted;
    }
};

int main() {
    string key = "CIPHERKEY";
    PlayfairCipher playfair(key);
    string plaintext = "HELLO123";
    string encrypted = playfair.encrypt(plaintext);
    
    cout << "Playfair Cipher:" << endl;
    cout << "Plaintext: " << plaintext << endl;
    cout << "Encrypted: " << encrypted << endl;
    
    vector<vector<int>> hillKey = {{6, 24, 1}, {13, 16, 10}, {20, 17, 15}};
    HillCipher hill(hillKey);
    string hillPlaintext = "ACT";
    string hillEncrypted = hill.encrypt(hillPlaintext);
    
    cout << "\nHill Cipher:" << endl;
    cout << "Plaintext: " << hillPlaintext << endl;
    cout << "Encrypted: " << hillEncrypted << endl;
    
    return 0;
}