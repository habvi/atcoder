use std::io::stdin;
use std::str::FromStr;

fn input_t<T: FromStr>() -> T {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    s.trim().parse().ok().unwrap()
}

fn main() {
    let q: usize = input_t();

    match q {
        1 => println!("ABC"),
        2 => println!("chokudai"),
        _ => unreachable!(),
    }
}
