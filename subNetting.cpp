#include <iostream>
#include <vector>
#include <bitset>
#include <sstream>
using namespace std;

vector<int> parseIP(const string &ip) {
    vector<int> parts;
    stringstream ss(ip);
    string segment;
    while (getline(ss, segment, '.')) {
        parts.push_back(stoi(segment));
    }
    return parts;
}

string calculateSubnetMask(int prefix) {
    unsigned int mask = 0xFFFFFFFF << (32 - prefix);
    return to_string((mask >> 24) & 0xFF) + "." + to_string((mask >> 16) & 0xFF) + "." +
           to_string((mask >> 8) & 0xFF) + "." + to_string(mask & 0xFF);
}

string calculateNetworkAddress(vector<int> ip, int prefix) {
    unsigned int mask = 0xFFFFFFFF << (32 - prefix);
    // cout<<ip[0]<<" ";
    // cout<<ip[1]<<" ";
    // cout<<ip[2]<<" ";
    // cout<<ip[3]<<" ";
    return to_string(ip[0] & (mask >> 24)) + "." + to_string(ip[1] & (mask >> 16)) + "." +
           to_string(ip[2] & (mask >> 8)) + "." + to_string(ip[3] & mask);
}

string calculateBroadcastAddress(vector<int> ip, int prefix) {
    unsigned int mask = 0xFFFFFFFF << (32 - prefix);
    unsigned int invertedMask = ~mask;
    cout<<to_string(invertedMask)<<endl;
    return to_string(ip[0] | (invertedMask >> 24)) + "." + to_string(ip[1] | (invertedMask >> 16)) + "." +
           to_string(ip[2] | (invertedMask >> 8)) + "." + to_string(ip[3] | invertedMask);
}

int main() {
    string ip;
    int prefix;
    
    cout << "Enter IP address (e.g., 192.168.1.0): ";
    cin >> ip;
    cout << "Enter subnet prefix (e.g., 24): ";
    cin >> prefix;
    
    vector<int> ipParts = parseIP(ip);
    
    cout << "Network Address: " << calculateNetworkAddress(ipParts, prefix) << endl;
    cout << "Subnet Mask: " << calculateSubnetMask(prefix) << endl;
    cout << "Broadcast Address: " << calculateBroadcastAddress(ipParts, prefix) << endl;
    cout << "Total Usable Hosts: " << (1 << (32 - prefix)) - 2 << endl;
    
    return 0;
}
