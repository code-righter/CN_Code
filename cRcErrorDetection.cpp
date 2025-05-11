#include <iostream>
#include <vector>

using namespace std;

// Function to get the frame from the user
vector<int> getFrame() {
    int fs;
    cout << "\n Enter Frame size: ";
    cin >> fs;
    vector<int> f(fs);
    cout << "\n Enter Frame:";
    for (int i = 0; i < fs; ++i) {
        cin >> f[i];
    }
    return f;
}

// Function to get the generator from the user
vector<int> getGenerator() {
    int gs;
    cout << "\n Enter Generator size: ";
    cin >> gs;
    vector<int> g(gs);
    cout << "\n Enter Generator:";
    for (int i = 0; i < gs; ++i) {
        cin >> g[i];
    }
    return g;
}

// Function to display binary data
void displayData(const string& message, const vector<int>& data) {
    cout << "\n " << message << ": ";
    for (int bit : data) {
        cout << bit;
    }
    cout << endl;
}

// Function to append zeros to the frame
vector<int> appendZerosToFrame(vector<int> frame, int numZeros) {
    for (int i = 0; i < numZeros; ++i) {
        frame.push_back(0);
    }
    return frame;
}

// Function to perform binary division
vector<int> performDivision(vector<int> dividend, const vector<int>& divisor) {
    int dividendSize = dividend.size();
    int divisorSize = divisor.size();

    for (int i = 0; i <= dividendSize - divisorSize; ++i) {
        if (dividend[i] >= divisor[0]) {
            for (int j = 0; j < divisorSize; ++j) {
                dividend[i + j] = dividend[i + j] ^ divisor[j];
            }
        }
    }
    vector<int> remainder(divisorSize - 1);
    for (int i = 0; i < divisorSize - 1; ++i) {
        remainder[i] = dividend[dividendSize - divisorSize + 1 + i];
    }
    return remainder;
}

// Function to generate the transmitted frame
vector<int> generateTransmittedFrame(const vector<int>& frame, const vector<int>& crc) {
    vector<int> transmittedFrame = frame;
    transmittedFrame.insert(transmittedFrame.end(), crc.begin(), crc.end());
    return transmittedFrame;
}

// Function to check for errors at the receiver side
bool checkError(const vector<int>& remainder) {
    for (int bit : remainder) {
        if (bit != 0) {
            return true; // Error detected
        }
    }
    return false; // No error
}

int main() {
    // Sender side
    vector<int> frame = getFrame();
    vector<int> generator = getGenerator();

    cout << "\n Sender Side:";
    displayData("Frame", frame);
    displayData("Generator", generator);

    int remainderSize = generator.size() - 1;
    cout << "\n Number of 0's to be appended: " << remainderSize;
    vector<int> augmentedFrame = appendZerosToFrame(frame, remainderSize);
    displayData("Message after appending 0's", augmentedFrame);

    vector<int> crc = performDivision(augmentedFrame, generator);
    displayData("CRC bits", crc);

    vector<int> transmittedFrame = generateTransmittedFrame(frame, crc);
    displayData("Transmitted Frame", transmittedFrame);

    // Receiver side
    cout << "\n Receiver side : ";
    displayData("Received Frame", transmittedFrame);

    vector<int> receiverRemainder = performDivision(transmittedFrame, generator);
    displayData("Remainder", receiverRemainder);

    if (!checkError(receiverRemainder)) {
        cout << "\n Since Remainder Is 0 Hence Message Transmitted From Sender To Receiver Is Correct" << endl;
    } else {
        cout << "\n Since Remainder Is Not 0 Hence Message Transmitted From Sender To Receiver Contains Error" << endl;
    }

    return 0;
}