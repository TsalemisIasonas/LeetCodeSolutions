class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> temperatures = {};
        temperatures.push_back(celsius + 273.15);
        temperatures.push_back(celsius*1.80 + 32.00);
        return temperatures;
    }
};