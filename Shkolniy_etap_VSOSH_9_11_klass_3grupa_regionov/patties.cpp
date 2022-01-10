#include <iostream>

long long int calculateNextBuy(long long int todaysPurchase)
{
	if (todaysPurchase == 1)
		return 2;
	else if (todaysPurchase == 2)
		return 3;
	else if (todaysPurchase == 3)
		return 1;
}

int main()
{
	using namespace std;
	long long int cranberriesPrice;
	long long int blueberriesPrice;
	long long int cherriesPrice;
	long long int days;
	long long int buyToday;
	long long int totalSpent = 0;
	cin >> cranberriesPrice;
	cin >> blueberriesPrice;
	cin >> cherriesPrice;
	cin >> days;
	cin >> buyToday;

	if (buyToday == 1)
		totalSpent += cranberriesPrice;
	else if (buyToday == 2)
		totalSpent += blueberriesPrice;
	else if (buyToday == 3)
		totalSpent += cherriesPrice;
	for (int i = 1; i < days; i++)
	{
		if (calculateNextBuy(buyToday) == 1)
			totalSpent += cranberriesPrice;
		if (calculateNextBuy(buyToday) == 2)
			totalSpent += blueberriesPrice;
		if (calculateNextBuy(buyToday) == 3)
			totalSpent += cherriesPrice;
		buyToday = calculateNextBuy(buyToday);
	}
	cout << totalSpent;
}
