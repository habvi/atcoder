#include <deque>
#include <iostream>
#include <string>

typedef std::pair<int, int> Pair;
typedef std::deque<Pair>    Deque;

int main() {
	int N, Q;
	std::cin >> N >> Q;

	Deque d;
	for (int i = 0; i < N; i++) {
		d.push_back({i + 1, 0});
	}
	for (int i = 0; i < Q; i++) {
		int x;
		std::cin >> x;
		if (x == 1) {
			std::string C;
			std::cin >> C;
			Pair p = d.front();
			if (C == "U") {
				p.second++;
			} else if (C == "D") {
				p.second--;
			} else if (C == "L") {
				p.first--;
			} else {
				p.first++;
			}
			d.pop_back();
			d.push_front({p.first, p.second});
		} else {
			int p;
			std::cin >> p;
			p--;
			std::cout << d[p].first << " " << d[p].second << std::endl;
		}
	}
}
