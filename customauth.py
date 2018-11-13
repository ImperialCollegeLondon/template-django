import ldap
import ldap.filter
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

# is_superuser = []
# is_staff = []
# is_user = []


class LdapBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        ldap_conn = ldap.initialize("ldap://icadsldap.ic.ac.uk")
        ldap_conn.set_option(ldap.OPT_REFERRALS, 0)
        ldap_conn.set_option(ldap.OPT_NETWORK_TIMEOUT, 5)
        ldap_conn.start_tls_s()
        try:
            ldap_conn.simple_bind_s(
                "%s@ic.ac.uk" % ldap.filter.escape_filter_chars(username, 1), password
            )
        except ldap.INVALID_CREDENTIALS:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            l_search_res = ldap_conn.search_s(
                "dc=ic,dc=ac,dc=uk", ldap.SCOPE_SUBTREE, f"(cn={username})"
            )[0]
            if l_search_res[0] is None:
                return None
            # if username not in is_staff + is_superuser + is_user:
            #     return None
            user = User(
                username=username,
                first_name=l_search_res[1]["givenName"][0].decode("utf-8"),
                last_name=l_search_res[1]["sn"][0].decode("utf-8"),
                email=l_search_res[1]["mail"][0].decode("utf-8"),
                # is_staff=username in is_staff or username in is_superuser,
                # is_superuser=username in is_superuser,
            )
            user.save()
        finally:
            ldap_conn.unbind()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
