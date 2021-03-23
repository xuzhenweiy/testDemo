import uiautomator2 as u2,time

d = u2.connect_usb(r"127.0.0.1:62025")

print(d.info)

# d.app_start('cn.cntvnews')
#
#
# # time.sleep(5)
#
# d.app_stop('cn.cntvnews')

# d(text='VR丨跟着总书记的脚步 走进武夷山').click()

#文本定位 并寻找元素是否存在 返回布尔
# ret = d(text='我的').exists
# print(ret)

#resourceId
# ret = d(resourceId='cn.cntvnews:id/rbUser')


#className
d(className='android.widget.RadioButton')[0].click()

