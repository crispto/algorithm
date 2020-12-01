use std::str;

extern crate base64;

pub fn encode(v: &str) -> String {
    let b64 = base64::encode_config(v, base64::STANDARD);
    return b64;
}

pub fn decode(v: &str) -> Result<String, String> {
    let v = base64::decode_config(v, base64::STANDARD);
    match v {
        Ok(u) => {
            let k = str::from_utf8(&u);
            match k {
                Ok(i) => Ok(String::from(i)),
                Err(e) => Err(e.to_string()),
            }
        }
        Err(e) => Err(e.to_string()),
    }
}
