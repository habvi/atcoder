use std::cmp::max;
use std::io::stdin;
use std::str::FromStr;

fn input_t<T: FromStr>() -> T {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    s.trim().parse().ok().unwrap()
}

fn main() {
    let n: usize = input_t();
    let mut total: usize = 0;
    let mut mx: usize = 0;
    for _ in 0..n {
        let p: usize = input_t();
        total += p;
        mx = max(mx, p);
    }
    println!("{}", total - mx / 2);
}
