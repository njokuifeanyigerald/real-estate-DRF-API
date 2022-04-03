class ContactView(GenericAPIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ContactSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            resume = data["resume"]
            # resume.name - file name
            # resume.read() - file contens
            return Response({"success": "True"})
        return Response({'success': "False"}, status=status.HTTP_400_BAD_REQUEST)