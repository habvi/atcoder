use std::io::stdin;
use std::str::FromStr;
use std::collections::{HashSet, HashMap};

fn input_t<T: FromStr>() -> T {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    s.trim().parse().ok().unwrap()
}

fn input_vec<T: FromStr>() -> Vec<T> {
    input_t::<String>()
        .split_whitespace()
        .map(|e| e.parse().ok().unwrap())
        .collect()
}

fn main() {
    let nm: Vec<usize> = input_vec();
    let (n, m) = (nm[0], nm[1]);
    let d: Vec<i64> = input_vec();
    let (a, b, c, d, e, f) = (d[0], d[1], d[2], d[3], d[4], d[5]);
    let mut ng: HashSet<(i64, i64)> = HashSet::new();
    for _ in 0..m {
        let xy: Vec<i64> = input_vec();
        let (x, y) = (xy[0], xy[1]);
        ng.insert((x, y));
    }
    const MOD: usize = 998244353;

    let mut dp: HashMap<(i64, i64), usize> = HashMap::new();
    dp.insert((0, 0), 1);
    for _ in 0..n {
        let mut ndp: HashMap<(i64, i64), usize> = HashMap::new();
        for ((x, y), v) in dp {
            for (dx, dy) in vec![(a, b), (c, d), (e, f)] {
                let nx = x + dx;
                let ny = y + dy;
                if ng.contains(&(nx, ny)) {
                    continue;
                }
                let tmp = ndp.entry((nx, ny)).or_insert(0);
                *tmp += v;
                *tmp %= MOD;
            }
        }
        dp = ndp;
    }

    let mut ans: usize = 0;
    for v in dp.values() {
        ans += v;
        ans %= MOD;
    }
    println!("{}", ans);
}
