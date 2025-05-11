#include <iostream>
#include <vector>
using namespace std;

// Function to calculate and insert parity bits (MSB to LSB)
vector<int> generateHammingCode(vector<int> data) {
    int m = data.size();
    int r = 0;

    // Find how many parity bits are needed
    while ((1 << r) < (m + r + 1)) {
        r++;
    }

    int totalBits = m + r;
    vector<int> hamming(totalBits + 1, 0); // 1-based indexing

    // Insert data bits into non-parity positions (from MSB to LSB)
    int dataIndex = 0;
    for (int i = totalBits; i >= 1; i--) {
        if ((i & (i - 1)) != 0) { // if i is not power of 2
            hamming[i] = data[dataIndex++];
        }
    }

    // Calculate parity bits
    for (int i = 0; i < r; i++) {
        int parityPos = 1 << i;
        int parity = 0;

        for (int j = 1; j <= totalBits; j++) {
            if (j & parityPos) {
                parity ^= hamming[j];
            }
        }

        hamming[parityPos] = parity;
    }

    return hamming;
}

// Introduce an error at a given position
vector<int> introduceError(vector<int> hamming, int pos) {
    if (pos >= 1 && pos < hamming.size()) {
        hamming[pos] ^= 1;
    }
    return hamming;
}

// Detect and correct single-bit error
int detectAndCorrect(vector<int>& hamming) {
    int n = hamming.size() - 1;
    int r = 0;

    while ((1 << r) <= n) r++;

    int errorPos = 0;
    for (int i = 0; i < r; i++) {
        int pos = 1 << i;
        int parity = 0;

        for (int j = 1; j <= n; j++) {
            if (j & pos) {
                parity ^= hamming[j];
            }
        }

        if (parity != 0) errorPos += pos;
    }

    if (errorPos != 0 && errorPos <= n) {
        hamming[errorPos] ^= 1;  // Correct the error
    }

    return errorPos;
}

// Helper to print vector
void printBits(const vector<int>& bits) {
    for (int i = 1; i < bits.size(); i++) {
        cout << bits[i];
    }
    cout << endl;
}

int main() {
    string input = "A"; // ASCII of A is 1000001
    int ascii = static_cast<int>(input[0]);

    vector<int> dataBits;
    for (int i = 6; i >= 0; i--) {
        dataBits.push_back((ascii >> i) & 1);
    }

    cout << "Original Data: ";
    for (int bit : dataBits) cout << bit;
    cout << endl;

    vector<int> hamming = generateHammingCode(dataBits);
    cout << "Hamming Code:  ";
    printBits(hamming);

    // Introduce an error at position 3
    vector<int> corrupted = introduceError(hamming, 3);
    cout << "With Error:    ";
    printBits(corrupted);

    int errorPos = detectAndCorrect(corrupted);
    if (errorPos == 0)
        cout << "No error detected.\n";
    else
        cout << "Error found and corrected at position: " << errorPos << endl;

    cout << "Corrected:     ";
    printBits(corrupted);

    return 0;
}
