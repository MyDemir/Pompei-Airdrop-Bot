Referans doğrulama kodlarını eklemek için, kullanıcının davet edildiği 
kişinin kullanıcı kimliğini saklamak için bir "ref" alanı eklemelisiniz.
 Örneğin, "users" adlı bir MongoDB koleksiyonunda saklarsanız, 
her kullanıcının "ref" alanının kimin tarafından davet edildiğini tutabilecek.
Davet eden kişinin referans sayısını arttırmak için, kullanıcının kaydolduğu anda, 
davet eden kişinin kaydını bulun ve "refCount" alanını arttırın. 
Ayrıca, davet eden kişinin "refList" alanına davet edilen kişinin kullanıcı kimliğini ekleyin.

Aşağıda, bu işlemleri gerçekleştiren örnek bir kod bloğu veriyorum:
Bu kod bloğu, kullanıcının davet edildiği kişinin kullanıcı kimliğini alır 
ve eğer davet eden kişi kayıtlı ise, onun "refCount" alanını arttırır ve 
davet edilen kişinin kullanıcı kimliğini "refList" alanına ekler.

def process_referral(user_id, referral_id):
    referral_user = users.find_one({"userId": referral_id})
    if referral_user:
        referral_user["refCount"] += 1
        referral_user["refList"].append(user_id)
        users.update_one({"userId": referral_id}, {"$set": referral_user})

def start(update, context):
    user = update.message.from_user
    referral_code = update.message.text.replace("/start", "").strip()
    if referral_code != "" and referral_code != user.id:
        process_referral(user.id, referral_code)
    # rest of the code


Bu kod bloğu, kullanıcının davet edildiği kişinin kullanıcı kimliğini alır 
ve eğer davet eden kişi kayıtlı ise, onun "refCount" alanını arttırır ve
 davet edilen kişinin kullanıcı kimliğini "refList" alanına ekler.

    if refferal != "" and refferal != user.id:
        ref_info = getUserInfo(int(refferal))
        if ref_info != "":
            ref_info["refCount"] += 1
            users.update({"userId": refferal}, ref_info)

Referansın geçerli olup olmadığını kontrol etme

    if refferal != "" and refferal != user.id:
        ref_info = getUserInfo(int(refferal))
        if ref_info == "":
            update.message.reply_text("Invalid referral link, please try again")
            return
        else:
            # valid referral, proceed with registration process
