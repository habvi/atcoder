use std::io::stdin;
use std::str::FromStr;

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
    let nk: Vec<usize> = input_vec();
    let k: usize = nk[1];
    let hs: Vec<usize> = input_vec();

    let mut ans: usize = 0;
    for h in hs {
        if h >= k {
            ans += 1;
        }
    }
    println!("{}", ans);
}
