use std::io::stdin;
use std::str::FromStr;
use std::collections::HashMap;

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
    #[allow(unused_variables)]
    let n: usize = input_t();
    let v: Vec<i64> = input_vec();

    let mut mp = HashMap::new();
    for a in v {
        *mp.entry(a).or_insert(0) += 1;
    }
    let k: Vec<_> = mp.keys().collect();
    let m = k.len();

    let mut ans = 0;
    for i in 0..m {
        for j in i + 1..m {
            let (a, b) = (k[i], k[j]);
            ans += (a - b).pow(2) * mp[a] * mp[b];
        }
    }
    println!("{}", ans);
}
