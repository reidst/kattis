// kattis-tle
use std::{collections::VecDeque, io::stdin};

fn asreg(x: u16) -> u16 {
    x & 0xfff
}

fn orwith(reg: u16, v: u16) -> u16 {
    reg | v
}

fn lsl(reg: u16, amt: u16) -> u16 {
    asreg(((reg as u32) << amt) as u16)
}

fn ror(reg: u16, amt: u16) -> u16 {
    if amt == 0 {
        reg
    } else {
        let rot = reg / 2;
        let low = reg & 1;
        ror(rot | (low << 11), amt - 1)
    }
}

fn addone(reg: u16) -> u16 {
    asreg(reg + 1)
}

fn not(reg: u16) -> u16 {
    asreg(!reg)
}

fn addshift(reg: u16, amt: u16) -> u16 {
    let shifted = asreg(reg << amt);
    orwith(reg, shifted)
}

fn solve(x: u16) -> usize {
    let mut q = VecDeque::new();
    q.push_back((0, 0));
    while let Some((reg, dist)) = q.pop_front() {
        if reg == x {
            return dist
        }
        let newdist = dist + 1;
        for v in 0..0xf {
            q.push_back((orwith(reg, v), newdist));
        }
        for amt in 0..0x7 {
            q.push_back((lsl(reg, amt), newdist));
            q.push_back((ror(reg, amt), newdist));
            q.push_back((addshift(reg, amt), newdist));
        }
        q.push_back((addone(reg), newdist));
        q.push_back((not(reg), newdist));
    }
    panic!("failed to find target")
}

fn read_int() -> u16 {
    let mut input = String::new();
    stdin().read_line(&mut input).expect("failed to read line");
    input.trim().parse().expect("failed to parse u16")
}

fn main() {
    let n = read_int();
    for _ in 0..n {
        let x = read_int();
        println!("{0}", solve(x));
    }
}
